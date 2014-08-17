'use strict';

memoryApp.factory('AuthService', function ($http, API_SERVER) {

  var register = function (username, password) {
    var url = API_SERVER + 'register/';
    $http.post(url, {
      username: username,
      password: password
    }, {
      headers: {
        'Content-Type': 'application/json'
      }
    }).then(
      function (response) {
        var token = response.data.token;
        var username = response.data.username;

        if (token && username) {
          $window.localStorage.token = token;
          $window.localStorage.username = username;
          //success
        } else {
          // error
        }
      },
      function (response) {
        // error callback
      }
    );
  };

  return {
    register: function (username, password) {
      return register(username, password);
    }
  };

});