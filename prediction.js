// Sample prediction function
async function predictAQI(location) {
    const response = await fetch('/api/predict', {
        method: 'POST',
        body: JSON.stringify({ location })
    });
    return await response.json();
}

// Example usage
document.getElementById('predict-btn').addEventListener('click', async () => {
    const location = document.getElementById('location-input').value;
    const prediction = await predictAQI(location);
    updateDashboard(prediction);
});
