import React, { useState } from 'react';
import Upload from './components/Upload';
import HeatmapView from './components/HeatmapView';

function App() {
  const [result, setResult] = useState(null);

  return (
    <div style={{ padding: 20 }}>
      <h2>Mirage - ELA Demo</h2>
      <Upload onResult={setResult} />
      <hr />
      <HeatmapView result={result} />
    </div>
  );
}

export default App;
