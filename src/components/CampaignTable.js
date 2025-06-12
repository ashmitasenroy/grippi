import React from "react";
import "../App.css";

function CampaignTable({ campaigns }) {
  return (
    <table className="campaign-table">
      <thead>
        <tr>
          <th>Campaign Name</th>
          <th>Status</th>
          <th>Clicks</th>
          <th>Cost ($)</th>
          <th>Impressions</th>
        </tr>
      </thead>
      <tbody>
        {campaigns.map((c) => (
          <tr key={c.id}>
            <td>{c.name}</td>
            <td><span className={`status-${c.status.toLowerCase()}`}>{c.status}</span></td>
            <td>{c.clicks}</td>
            <td>{c.cost.toFixed(2)}</td>
            <td>{c.impressions}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default CampaignTable;
