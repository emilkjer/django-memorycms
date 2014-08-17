'use strict';

app.controller('AppAllCtrl', function($scope, $http, AuthService, API_SERVER) {
    var url = API_SERVER + 'apps/';
    $http.get(url).success(function(result){
        $scope.result = result;
    }).error(function(error){
        $scope.error = error;
    });
    }
);

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
    }
);


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
    }
);