var memoryApp = angular.module('memoryApp', [
  'ngRoute',
  'memoryCMSControllers'
]);

memoryApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/apps', {
        templateUrl: 'partials/app-all.html',
        controller: 'AppAllCtrl'
      }).
      when('/apps/:appId', {
        templateUrl: 'partials/app-detail.html',
        controller: 'AppDetailCtrl'
      }).
      when('/apps/:appId/group/:groupId', {
        templateUrl: 'partials/app-detail.html',
        controller: 'GroupDetailCtrl'
      }).
      otherwise({
        redirectTo: '/apps'
      });
}]);


memoryApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

memoryApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.headers.common['X-CSRFToken'] = '{{ csrf_token|escapejs }}';
}]);