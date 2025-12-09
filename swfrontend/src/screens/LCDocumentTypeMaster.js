import React, { useEffect, useState } from 'react';

const LCDocumentTypeMaster = () => {
  const [docs, setDocs] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api/master/lc-document-type/')
      .then(res => {
        if (!res.ok) throw new Error('Failed to fetch');
        return res.json();
      })
      .then(data => setDocs(data))
      .catch(err => {
        console.error('Error fetching LC Document Type data:', err);
        setError('Unable to load data');
      });
  }, []);

  return (
    <div>
      <h2>LC Document Type Master</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <ul>
        {docs.map(doc => (
          <li key={doc.id}>{doc.doc_name}</li>
        ))}
      </ul>
    </div>
  );
};

export default LCDocumentTypeMaster;