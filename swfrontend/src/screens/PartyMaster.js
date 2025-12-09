import React, { useEffect, useState } from 'react';

const PartyMaster = () => {
  const [parties, setParties] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api/master/party-master/')
      .then(res => {
        if (!res.ok) throw new Error('Failed to fetch');
        return res.json();
      })
      .then(data => setParties(data))
      .catch(err => {
        console.error('Error fetching Party Master data:', err);
        setError('Unable to load data');
      });
  }, []);

  return (
    <div>
      <h2>Party Master</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <ul>
        {parties.map(party => (
          <li key={party.id}>{party.party_name}</li>
        ))}
      </ul>
    </div>
  );
};

export default PartyMaster;