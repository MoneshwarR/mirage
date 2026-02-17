import React from 'react';

export default function HeatmapView({ result }) {
  if (!result) return <div>No result yet.</div>;
  if (result.error) return <div>Error: {result.error}</div>;
  // expected result { heatmap_b64: "...", ela_score: 0.12 }
  return (
    <div>
      <h3>ELA Heatmap</h3>
      {result.heatmap_b64 ? (
        <img alt="ELA heatmap" src={`data:image/png;base64,${result.heatmap_b64}`} style={{ maxWidth: '100%' }} />
      ) : (
        <pre>{JSON.stringify(result, null, 2)}</pre>
      )}
      {result.ela_score !== undefined && <p>ELA score: {result.ela_score}</p>}
    </div>
  );
}
