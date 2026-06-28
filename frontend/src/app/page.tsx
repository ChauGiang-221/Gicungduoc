import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24 bg-slate-50 dark:bg-slate-900">
      <div className="z-10 max-w-5xl w-full items-center justify-center font-mono text-sm flex flex-col gap-8">
        <h1 className="text-4xl md:text-6xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-indigo-600 dark:from-blue-400 dark:to-indigo-400 text-center">
          VN AI Innovation
        </h1>

        <p className="text-xl text-slate-600 dark:text-slate-300 text-center max-w-2xl">
          Sẵn sàng xây dựng giải pháp AI cho Việt Nam
        </p>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 w-full max-w-3xl mt-8">
          <div className="p-6 bg-white dark:bg-slate-800 rounded-xl shadow-sm border border-slate-200 dark:border-slate-700">
            <h2 className="text-xl font-semibold mb-2">Frontend Stack</h2>
            <ul className="list-disc list-inside space-y-1 text-slate-600 dark:text-slate-400">
              <li>Next.js 15 (App Router)</li>
              <li>Tailwind CSS</li>
              <li>Shadcn UI</li>
              <li>Lucide Icons</li>
            </ul>
          </div>

          <div className="p-6 bg-white dark:bg-slate-800 rounded-xl shadow-sm border border-slate-200 dark:border-slate-700">
            <h2 className="text-xl font-semibold mb-2">Backend Stack</h2>
            <ul className="list-disc list-inside space-y-1 text-slate-600 dark:text-slate-400">
              <li>FastAPI</li>
              <li>OpenAI | Claude | Gemini</li>
              <li>Firebase Firestore</li>
              <li>Pydantic Validation</li>
            </ul>
          </div>
        </div>

        <div className="flex gap-4 mt-8">
          <Button size="lg" className="px-8">
            Bắt đầu khám phá
          </Button>
          <Button variant="outline" size="lg" className="px-8" asChild>
            <a href="http://localhost:8000/docs" target="_blank" rel="noopener noreferrer">
              Xem API Docs
            </a>
          </Button>
        </div>
      </div>
    </main>
  );
}
