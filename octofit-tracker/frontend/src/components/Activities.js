import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        setLoading(false);
        console.log('Activities endpoint:', endpoint);
        console.log('Activities data:', results);
      });
  }, [endpoint]);

  if (loading) return <div className="text-center">Loading...</div>;

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Activities</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>Type</th>
            <th>Duration</th>
            <th>Distance</th>
            <th>User</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {data.map(activity => (
            <tr key={activity.id}>
              <td>{activity.id}</td>
              <td>{activity.type}</td>
              <td>{activity.duration}</td>
              <td>{activity.distance}</td>
              <td>{activity.user}</td>
              <td>{activity.timestamp}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Activities;
