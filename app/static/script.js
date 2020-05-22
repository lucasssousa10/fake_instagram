$(function() {
    if (navigator.geolocation) 
    {
        navigator.geolocation.getCurrentPosition((position) => 
        {
            let coordenadas = "Latitude: " + position.coords.latitude + "<br>Longitude: " + position.coords.longitude;
            console.log(coordenadas);
            $("#coords").prop('innerHTML', coordenadas);
        });
    } else {
        $("#coords").prop('innerHTML', "Geolocation is not supported by this browser.");
    }
});