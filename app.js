const APIController = (function() {

    const clientId = "f572cf52d72b4e44ac55d6c14ba6f74a";
    const clientSecret = "18f76a14e1554ad69b2d51070a9a67eb" ;

    //private method
    const _getToken = async () => {

        const result = await fetch ("https://accounts.spotify.com/api/token", {
            method: "POST",
            headers: {
                "Content-Type" : "application/x-www-form-urlencoded",
                "Autorization" : "Basic " + btoa(clientID + ":" + clientSecret)
            },
            body: "grant_type=client_credentials"
        });

        const data = await result.json();
        return data.access_token;
    }

    const _getSearch = async (token) => {

        const result = await fetch('https://api.spotify.com/v1/search', {
            method: "GET",
            headers: { "Authorization" : "Bearer " + token}
        });

        const data = await result.json();
        return data;

    }



    return {
        getToken(){
            return _getToken();
        },
        getSearch(){
            return _getSearch(token, trackEndPoint);
        }
    }

})();

//UI Module
const UIController = (function() {

    //object to hold references to html selectors
    const DOMElements = {



    }

    //return

})



