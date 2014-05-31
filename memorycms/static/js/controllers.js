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
        $http.get('/api/app/'+$routeParams.appId+'/')
            .success(function(result){
                $scope.result = result;
                $scope.groupId = result.top_group_id;
            }
        );
    }
]);

memoryCMSControllers.controller('GroupDetailCtrl', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http) {
        $scope.appId = $routeParams.appId;
        $scope.groupId = $routeParams.groupId;
        $scope.result = [];
        //TODO make this call to service
        //TODO make faulty callback
        $http.get('/api/app/'+$routeParams.groupId+'/get_group_content/')
            .success(function(result){
                $scope.result = result;
            });
    }
]);

memoryCMSControllers.controller('AddTextCtrl', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http){
        $scope.text = '';
        $scope.groupId = $routeParams.groupId;
        $scope.appId = $routeParams.appId;
        $scope.result = '';

        $scope.submit = function() {
            $http.post('/api/app/'+$routeParams.groupId+'/add_text/', {'content': this.text })
                .success(function(data) {
                    console.log('submitted!');
                    $scope.result = data;
                });
            $scope.text = this.text;
            console.log(this.text);

        };
    }
]);

memoryCMSControllers.controller('AddStringCtrl', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http){
        $scope.text = '';
        $scope.groupId = $routeParams.groupId;
        $scope.appId = $routeParams.appId;
        $scope.result = '';

        $scope.submit = function() {
            $http.post('/api/app/'+$routeParams.groupId+'/add_string/', {'content': this.text })
                .success(function(data) {
                    console.log('submitted!');
                    $scope.result = data;
                });
            $scope.text = this.text;
            console.log(this.text);
        };
    }
]);

memoryCMSControllers.controller('AddGroupCtrl', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http){
        $scope.text = '';
        $scope.groupId = $routeParams.groupId;
        $scope.appId = $routeParams.appId;
        $scope.result = '';

        $scope.submit = function() {
            $http.post('/api/app/'+$routeParams.groupId+'/add_group/', {'content': this.text })
                .success(function(data) {
                    console.log('submitted!');
                    $scope.result = data;
                });
            $scope.text = this.text;
            console.log(this.text);
        };
    }
]);