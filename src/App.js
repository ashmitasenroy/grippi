import React, { useEffect, useState } from "react";
import FilterDropdown from "./components/FilterDropdown";
import CampaignTable from "./components/CampaignTable";
import "./App.css";

function App() {
  const [campaigns, setCampaigns] = useState([]);
  const [filter, setFilter] = useState("All");

  useEffect(() => {
    fetch("http://localhost:8000/campaigns")
      .then((res) => res.json())
      .then((data) => setCampaigns(data))
      .catch((error) => console.error("Error fetching campaigns:", error));
  }, []);

  const filteredCampaigns =
    filter === "All"
      ? campaigns
      : campaigns.filter((c) => c.status === filter);

  return (
    <div className="app-container">
      <h1> Campaign Analytics Dashboard</h1>
      <div className="dashboard-card">
        <FilterDropdown filter={filter} setFilter={setFilter} />
        <CampaignTable campaigns={filteredCampaigns} />
      </div>
    </div>
  );
}

export default App;
