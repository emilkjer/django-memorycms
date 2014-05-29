var memoryCMSControllers = angular.module('memoryCMSControllers', []);

memoryCMSControllers.controller('AppAllCtrl', ['$scope', '$http',
    function($scope, $http) {
        $http.get('/api/apps/').success(function(result){
            $scope.result = result;
        });
    }
]);

memoryCMSControllers.controller('AppDetailCtrl', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http) {
        $scope.appId = $routeParams.appId;
        $scope.result = [];
        //TODO make this call to service
        //TODO make faulty callback
        $http.get('/api/app/'+$routeParams.appId+'/').success(function(result){
            $scope.result = result;
        });
    }
]);

memoryCMSControllers.controller('GroupDetailCtrl', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http) {
        $scope.appId = $routeParams.appId;
        $scope.groupId = $routeParams.groupId;
        $scope.result = [];
        //TODO make this call to service
        //TODO make faulty callback
        $http.get('/api/app/'+$routeParams.groupId+'/get_group_content/').success(function(result){
            $scope.result = result;
        });
    }
]);
