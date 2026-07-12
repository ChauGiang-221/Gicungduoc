import './styles.css'

const API_URL = 'http://localhost:8000'

interface Message {
  role: 'user' | 'assistant'
  content: string
}

let messages: Message[] = []
let streaming = false

const messagesEl = document.getElementById('messages')!
const inputEl = document.getElementById('input') as HTMLInputElement
const sendBtn = document.getElementById('send')!

async function sendMessage() {
  const content = inputEl.value.trim()
  if (!content || streaming) return

  const userMsg: Message = { role: 'user', content }
  messages.push(userMsg)
  inputEl.value = ''
  streaming = true
  sendBtn.textContent = '...'
  sendBtn.disabled = true

  const assistantMsg: Message = { role: 'assistant', content: '' }
  messages.push(assistantMsg)
  renderMessages()

  try {
    const response = await fetch(`${API_URL}/chat/stream`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages }),
    })

    const reader = response.body?.getReader()
    if (!reader) return

    const decoder = new TextDecoder()
    let buffer = ''

    while (true) {
      const { done, value } = await reader.read()
      if (done) break

      buffer += decoder.decode(value)
      const lines = buffer.split('\n')
      buffer = lines.pop() || ''

      for (const line of lines) {
        if (line.startsWith('data: ')) {
          const data = line.slice(6)
          if (data === '[DONE]') continue
          try {
            const { content: text } = JSON.parse(data)
            if (text) {
              const last = messages[messages.length - 1]
              if (last.role === 'assistant') {
                last.content += text
                renderMessages()
              }
            }
          } catch {}
        }
      }
    }
  } catch (err) {
    const last = messages[messages.length - 1]
    if (last.role === 'assistant') {
      last.content = 'Lỗi kết nối'
      renderMessages()
    }
  }

  streaming = false
  sendBtn.textContent = 'Gửi'
  sendBtn.disabled = false
}

function renderMessages() {
  messagesEl.innerHTML = messages.length === 0
    ? '<p class="empty">Chào bạn! Tôi có thể giúp gì?</p>'
    : messages.map(m => `
        <div class="message ${m.role}">
          <p>${escapeHtml(m.content)}${m.role === 'assistant' && streaming && !m.content ? '...' : ''}</p>
        </div>
      `).join('')
  messagesEl.scrollTop = messagesEl.scrollHeight
}

function escapeHtml(text: string): string {
  return text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
}

sendBtn.addEventListener('click', sendMessage)
inputEl.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') sendMessage()
})
