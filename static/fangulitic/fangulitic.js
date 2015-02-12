"use strict";
/**
 * /static/client/main/fangulitic.js
 * -
 * main angular.js module
 */

// load angularjs modules
var Fangulitic = angular.module('fangulitic',
    [
        'ui.router',
        'ui.bootstrap'
    ]);

Fangulitic.config(
    function($stateProvider, $urlRouterProvider){

        $urlRouterProvider.otherwise('/public');

        $stateProvider
            .state('authenticated',{
                url: '/dashboard',
                templateUrl: '/static/fangulitic/partials/authenticated.html'
            })

            .state('unauthenticated',{

            });


    }
);

