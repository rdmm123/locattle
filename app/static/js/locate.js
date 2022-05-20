const initMap = () => {
    const map = L.map('map').setView([10.996, -74.808], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap;',
        maxZoom: 18,
    }).addTo(map);
    return map
}

const fetchLastLocation = async () => {
    const response = await fetch(locationEndpoint);
    const data = await response.json();
    return data
}

const formatData = (data) => {
    const timestampDate = Date(data.timestamp);
    const formattedDate = timestampDate.toLocaleString('es-CO', {'timeStyle': 'short'});
    return `
        <ul>
            <li><b>Latitud:</b> ${data.lat}</li>
            <li><b>Longitud:</b> ${data.lng}</li>
            <li><b>Timestamp:</b> ${timestampDate}</li>
            <li><b>Vaca:</b> ${data.cow}</li>
            <li><b>Finca:</b> ${data.farm}</li>
            <li><b>Departamento:</b> ${data.depto}</li>
        </ul>
    `
}

const setLocation = async (initial=false) => {
    const data = await fetchLastLocation();
    const latLng = [data.lat, data.lng];
    map.setView(latLng, 15);
    if (initial) {
        const popup = new L.popup({autoPan: false}).setContent(formatData(data));
        marker.bindPopup(popup).openPopup();
    }
    marker.setLatLng(latLng).addTo(map);
}

const map = initMap();
const marker = L.marker([]);
setLocation(true);
setInterval(setLocation, 10000);