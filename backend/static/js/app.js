'use strict';


var memoryApp = angular.module('memoryApp', [
  'ngRoute',
  'ngResource',
  'ngSanitize',
  'ngCookies',
  'memoryCMSControllers'
]).run(function($http, $cookies){
    // set the CSRF token here
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;

//    $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
});

memoryApp.config(['$routeProvider','$httpProfider',
    function($httpProvider) {
        $httpProvider.interceptors.push('AuthInterceptor')
    },


  function($routeProvider) {
        $routeProvider
        .when('/', {
            templateUrl: 'views/auth.html',
            controller: 'AuthCtrl'})
        .when('/apps', {
            templateUrl: 'partials/app-all.html',
            controller: 'AppAllCtrl'})
        .when('/login', {
            templateUrl: 'partials/login-page.html',
            controller: 'LoginCtrl'})
        .when('/logout', {
            templateUrl: 'partials/login-page.html',
            controller: 'LogoutCtrl'})
        .when('/apps/:appId', {
            templateUrl: 'partials/app-detail.html',
            controller: 'AppDetailCtrl'})
        .when('/apps/:appId/group/:groupId', {
            templateUrl: 'partials/app-detail.html',
            controller: 'GroupDetailCtrl'})
        .when('/apps/:appId/group/:groupId/add_text', {
            templateUrl: 'partials/app-add-text.html',
            controller: 'AddTextCtrl'})
        .when('/apps/:appId/group/:groupId/add_string', {
            templateUrl: 'partials/app-add-string.html',
            controller: 'AddStringCtrl'})
        .when('/apps/:appId/group/:groupId/add_group', {
            templateUrl: 'partials/app-add-group.html',
            controller: 'AddGroupCtrl'})
        .otherwise({
            redirectTo: '/'
        });
  }
]);


memoryApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

memoryApp.config(['$httpProvider', function($httpProvider) {
    // $httpProvider.defaults.headers.common['X-CSRFToken'] = '{{ csrf_token|escapejs }}';
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    // $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    // $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    // $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];

}]);

memoryApp.constant('API_SERVER', 'http://127.0.0.1:8000/api/');
