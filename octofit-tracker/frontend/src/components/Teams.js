import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('https://upgraded-space-adventure-65qrwpvj6phrxvj-8000.app.github.dev/api/teams/')
      .then(response => response.json())
      .then(data => setTeams(data))
      .catch(error => console.error('Error fetching teams:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Teams</h1>
      <ul className="list-group">
        {teams.map(team => (
          <li key={team.id} className="list-group-item">{team.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Teams;
