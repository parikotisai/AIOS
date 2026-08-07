import { useEffect, useState } from "react";

function App() {
  const [trace, setTrace] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/trace")
      .then((res) => res.json())
      .then((data) => setTrace(data));
  }, []);

  return <pre>{JSON.stringify(trace, null, 2)}</pre>;
}

export default App;
