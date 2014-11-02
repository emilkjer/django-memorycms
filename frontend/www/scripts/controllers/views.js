'use strict';

app.controller('AppAllCtrl', function($scope, $http, AuthService, API_SERVER) {
    var url = API_SERVER + 'apps/';
    $http.get(url).success(function(result){
        $scope.result = result;
    }).error(function(error){
        $scope.error = error;
    });
});

app.controller('AppDetailCtrl', function($scope, $routeParams, $http, AuthService, API_SERVER) {
    var url = API_SERVER + 'app/'+$routeParams.appId+'/';
    $scope.appId = $routeParams.appId;
    $scope.result = [];

    //TODO make this call to service
    $http.get(url)
        .success(function(result){
            $scope.result = result;
            $scope.groupId = result.top_group_id;
        }).error(function(error){
            $scope.error = error;
        });
});

//AddStringCtrl
app.controller('AddStringCtrl', function($scope, $routeParams, $http, AuthService, API_SERVER) {
    var url = API_SERVER + 'app/'+$routeParams.groupId+'/add_string/';
    $scope.appId = $routeParams.appId;
    $scope.groupId = $routeParams.groupId;

    $scope.mx = {};
    $scope.mx.text = "";

    $scope.mx.submitTheForm = function(item, event) {
       console.log("--> Submitting form");
       console.log($scope.mx);

       var dataObject = {
           content: $scope.mx.text
       };
        console.log("dataobject:");
        console.log(dataObject);

       var responsePromise = $http.post(url, dataObject,{
           withCredentials: true,
           headers: {
               'Content-Type': 'application/x-www-form-urlencoded'
       }});
       responsePromise.success(function(dataFromServer, status, headers, config) {
          console.log(dataFromServer.STATUS);
           console.log(dataFromServer.message);
       });
        responsePromise.error(function(data, status, headers, config) {
          alert("Submitting form failed!");
       });
     }
});

//
//app.controller('AddStringSubmitCtrl', function($scope, $routeParams, $http, AuthService, API_SERVER) {
////    var url = API_SERVER + 'app/'+$routeParams.groupId+'/get_group_content/';
//    $scope.appId = $routeParams.appId;
//    $scope.groupId = $routeParams.groupId;
//});


app.controller('GroupDetailCtrl', function($scope, $routeParams, $http, AuthService, API_SERVER) {
    var url = API_SERVER + 'app/'+$routeParams.groupId+'/get_group_content/';
    $scope.appId = $routeParams.appId;
    $scope.groupId = $routeParams.groupId;
    $scope.result = [];

    //TODO make this call to service
    $http.get(url)
        .success(function(result){
            $scope.result = result;
        }).error(function(error){
            $scope.error = error;
        });
});