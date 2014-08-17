'use strict';
/* global app: true */

var app = angular.module('frontendApp', [
    'ngCookies',
    'ngResource',
    'ngSanitize',
    'ngRoute'
]);

app.config(function ($routeProvider, $httpProvider) {
    $httpProvider.interceptors.push('AuthInterceptor');
    $routeProvider
        .when('/', {
            templateUrl: 'views/auth.html',
            controller: 'AuthCtrl'
        })
        .when('/dashboard', {
            templateUrl: 'views/dashboard.html',
            controller: 'DashboardCtrl'
        })
        .when('/my_user', {
            templateUrl: 'views/dashboard.html',
            controller: 'MyUserCtrl'
        })
        .when('/apps/:appId', {
            templateUrl: 'views/app_detail.html',
            controller: 'AppDetailCtrl'
        })
        .when('/apps/:appId/group/:groupId', {
            templateUrl: 'views/app_detail.html',
            controller: 'GroupDetailCtrl'
        })
        .when('/apps', {
            templateUrl: 'views/app_all.html',
            controller: 'AppAllCtrl'
        })    
        .otherwise({
            redirectTo: '/'
        });
});
app.constant('API_SERVER', 'http://127.0.0.1:5000/api/');
