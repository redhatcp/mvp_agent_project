import { useEffect, useState } from "react";
import { runAgent, getTasks } from "./api";

export default function App() {
  const [tasks, setTasks] = useState([]);
  const [agentName, setAgentName] = useState("");

  const refreshTasks = async () => {
    const data = await getTasks();
    setTasks(data);
  };

  const handleRun = async () => {
    if(!agentName) return;
    await runAgent(agentName);
    setAgentName("");
    refreshTasks();
  };

  useEffect(() => { refreshTasks(); }, []);

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-2">MVP Agent 控制台</h1>
      <input className="border p-1 mr-2" value={agentName} onChange={e => setAgentName(e.target.value)} placeholder="Agent Name"/>
      <button className="bg-blue-500 text-white px-2 py-1" onClick={handleRun}>运行 Agent</button>
      <ul className="mt-4">
        {tasks.map(t => <li key={t.id}>{t.id} | {t.name} | {t.status} | {t.result}</li>)}
      </ul>
    </div>
  );
}