import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [topic, setTopic] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!topic) {
      alert("Por favor, digite um tema!");
      return;
    }
    setLoading(true);
    try {
      const response = await axios.post("http://127.0.0.1:8000/generate_text", {
        topic,
      });
      setResult(response.data.generated_text);
    } catch (error) {
      console.error(error);
      alert("Erro ao gerar texto.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>🧠 Gerador de Textos Inteligente</h1>
      <textarea
        placeholder="Digite um tema..."
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />
      <button onClick={handleGenerate} disabled={loading}>
        {loading ? "Gerando..." : "Gerar"}
      </button>
      {result && (
        <div className="result">
          <h3>✨ Resultado:</h3>
          <p>{result}</p>
        </div>
      )}
    </div>
  );
}

export default App;
