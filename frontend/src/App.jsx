import { useEffect, useState } from "react";

function App() {
  const [trace, setTrace] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/trace")
      .then((res) => res.json())
      .then((data) => setTrace(data));
  }, []);

  if (trace == null) return <p>Loading trace ..</p>;

  return (
    <div>
      <p>Total steps : {trace.length}</p>
      <pre>{JSON.stringify(trace, null, 2)}</pre>
    </div>
  );
}

export default App;
