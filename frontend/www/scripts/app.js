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
        .when('/apps/:appId/group/:groupId/add-string', {
            templateUrl: 'views/add_string.html',
            controller: 'AddStringCtrl'
        })
        .when('/apps', {
            templateUrl: 'views/app_all.html',
            controller: 'AppAllCtrl'
        })    
        .otherwise({
            redirectTo: '/'
        });
});

//app.constant('API_SERVER', 'http://localhost:5000/api/');
app.constant('API_SERVER', 'http://apimemorycms.moome.net/api/');
