import React, { useEffect, useState } from 'react';

const BankMaster = () => {
  const [banks, setBanks] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api/master/bank-master/')
      .then(res => {
        if (!res.ok) throw new Error('Failed to fetch');
        return res.json();
      })
      .then(data => setBanks(data))
      .catch(err => {
        console.error('Error fetching Bank Master data:', err);
        setError('Unable to load data');
      });
  }, []);

  return (
    <div>
      <h2>Bank Master</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <ul>
        {banks.map(bank => (
          <li key={bank.id}>{bank.bank_name}</li>
        ))}
      </ul>
    </div>
  );
};

export default BankMaster;