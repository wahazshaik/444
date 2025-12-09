import React, { useEffect, useState } from 'react';

const PlantMaster = () => {
  const [plants, setPlants] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api/master/plant-master/')
      .then(res => {
        if (!res.ok) throw new Error('Failed to fetch');
        return res.json();
      })
      .then(data => setPlants(data))
      .catch(err => {
        console.error('Error fetching Plant Master data:', err);
        setError('Unable to load data');
      });
  }, []);

  return (
    <div>
      <h2>Plant Master</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <ul>
        {plants.map(plant => (
          <li key={plant.id}>{plant.plant_name}</li>
        ))}
      </ul>
    </div>
  );
};

export default PlantMaster;