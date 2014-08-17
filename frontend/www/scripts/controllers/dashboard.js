'use strict';

app.controller('DashboardCtrl', function ($scope, $window, $location, AuthService) {
  if (!$window.localStorage.token) {
    $location.path('/');
    return;
  }
  $scope.token = $window.localStorage.token;
  $scope.username = $window.localStorage.username;

  $scope.logout = function () {
    AuthService.logout().then(
      function () {
        $location.path('/');
      },
      function (error) {
        $scope.error = error;
      }
    );
  };
});

app.controller('MyUserCtrl', function ($scope, $window, $location, AuthService, $http, API_SERVER) {
  if (!$window.localStorage.token) {
    $location.path('/');
    return;
  }
  $scope.token = $window.localStorage.token;
  $scope.username = $window.localStorage.username;
  var url = API_SERVER + 'my_user/';
  $scope.url = url;
  $http.get(url).success(
    function(result){
      $scope.jazz = "Whoop this is jazz!";
      $scope.result = result;
    }
  ).error(
    function(result){
      $scope.jazz = "Blah there was an error";
      $scope.result = result;
    }
  );

  $scope.logout = function () {
    AuthService.logout().then(
      function () {
        $location.path('/');
      },
      function (error) {
        $scope.error = error;
      }
    );
  };

});


