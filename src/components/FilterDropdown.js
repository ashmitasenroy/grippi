import React from "react";

function FilterDropdown({ filter, setFilter }) {
  return (
    <div className="filter-dropdown">
      <label htmlFor="status-filter">Filter by Status: </label>
      <select
        id="status-filter"
        value={filter}
        onChange={(e) => setFilter(e.target.value)}
      >
        <option value="All">All</option>
        <option value="Active">Active</option>
        <option value="Paused">Paused</option>
      </select>
    </div>
  );
}

export default FilterDropdown;
