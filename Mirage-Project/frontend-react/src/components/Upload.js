import React, { useState } from 'react';
import api from '../services/api';

export default function Upload({ onResult }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const submit = async (e) => {
    e.preventDefault();
    if (!file) return;
    setLoading(true);
    const form = new FormData();
    form.append('file', file);
    try {
      const res = await api.post('/api/upload', form, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      onResult(res.data);
    } catch (err) {
      console.error(err);
      onResult({ error: 'Upload failed' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={submit}>
      <input type="file" accept="image/*" onChange={e => setFile(e.target.files[0])} />
      <button type="submit" disabled={loading || !file}>
        {loading ? 'Uploading...' : 'Upload'}
      </button>
    </form>
  );
}
