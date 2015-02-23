"use strict";
/**
 * /static/client/main/fangulitic.js
 * -
 * main angular.js module
 */

// load angularjs modules
var Fangulitic = angular.module('fangulitic',
    [
        'ui.utils',
        'ui.router',
        'ui.bootstrap',
        'ui.grid'
    ]
);

Fangulitic.config(
    function($stateProvider, $urlRouterProvider){

        $urlRouterProvider.otherwise('/public');

        $stateProvider
            .state('authenticated',{
                views: {

                    'headerView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/header.html'
                    },

                    'sidebarView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/sidebar.html',
                        controller: 'SidebarCtrl'
                    },

                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/content.html'
                    },

                    'footerView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/footer.html'
                    }

                }
            })

            .state('authenticated.dashboard',{
                url: '/dashboard',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'dashboard';
                            $scope.dashContent = DashService.getDashboard($scope.dashTitle);
                        }
                    }
                }
            })

            .state('authenticated.dashboard.logout', {
                url: '/logout',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'logout';
                            $scope.dashContent = 'Log out';
                        }
                    }
                }
            })

            .state('authenticated.pages',{
                url: '/pages',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'pages';
                            $scope.dashContent = DashService.getDashboard($scope.dashTitle);
                        }
                    }
                }
            })

            .state('authenticated.pages.platforms',{
                url: '/platforms',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'platforms';
                            $scope.dashContent = 'Platforms Content';
                        }
                    }
                }


            })

            .state('authenticated.pages.platforms.routing',{
                url: '/routing',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'routing';
                            $scope.dashContent = 'Routing Content';
                        }
                    }
                }


            })

            .state('authenticated.pages.platforms.switching',{
                url: '/switching',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'switching';
                            $scope.dashContent = 'Switching Content';
                        }
                    }
                }


            })

            .state('authenticated.pages.platforms.wireless',{
                url: '/wireless',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'wireless';
                            $scope.dashContent = 'Wireless Content';
                        }
                    }
                }


            })

            .state('authenticated.pages.solutions', {
                url: '/solutions',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'solutions';
                            $scope.dashContent = 'Solutions Content';
                        }
                    }
                }
            })

            .state('authenticated.pages.services', {
                url: '/services',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'services';
                            $scope.dashContent = 'Services Content';
                        }
                    }
                }
            })

            .state('authenticated.pages.training', {
                url: '/training',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'training';
                            $scope.dashContent = 'Training Content';
                        }
                    }
                }
            })

            .state('authenticated.pages.competitive', {
                url: '/competitive',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'competitive';
                            $scope.dashContent = 'Competitive Content';
                        }
                    }
                }
            })

            .state('authenticated.forum',{
                url: '/forum',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'forum';
                            $scope.dashContent = DashService.getDashboard($scope.dashTitle);
                        }
                    }
                }
            })

            .state('authenticated.contacts',{
                url: '/contacts',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'contacts';
                            $scope.dashContent = DashService.getDashboard($scope.dashTitle);
                        }
                    }
                }
            })

            .state('authenticated.metrics',{
                url: '/metrics',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'metrics';
                            $scope.dashContent = DashService.getDashboard($scope.dashTitle);
                        }
                    }
                }
            })

            .state('authenticated.admin',{
                url: '/admin',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'admin';
                            $scope.dashContent = DashService.getDashboard($scope.dashTitle);
                        }
                    }
                }
            })

            .state('authenticated.help',{
                url: '/help',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/authenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'help';
                            $scope.dashContent = 'Help Content';
                        }
                    }
                }
            })

            .state('unauthenticated',{
                url: '/public',
                views: {

                    'headerView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/unauthenticated/layout/header.html'
                    },

                    'sidebarView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/unauthenticated/layout/sidebar.html',
                        controller: 'SidebarCtrl'
                    },

                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/unauthenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'ENG-TME Dashboard';
                            $scope.dashContent = 'Login to view Content';
                        }
                    },

                    'footerView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/unauthenticated/layout/footer.html'
                    }

                }
            })

            .state('unauthenticated.dashboard',{
                url: '/dashboard',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/unauthenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'ENG-TME Dashboard';
                            $scope.dashContent = 'Login to view Content';
                        }
                    }
                }
            })

            .state('unauthenticated.dashboard.login',{
                url: '/login',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/unauthenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'login';
                            $scope.dashContent = 'Login Content';
                        }
                    }
                }
            })

            .state('unauthenticated.dashboard.register',{
                url: '/register',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/unauthenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'register';
                            $scope.dashContent = 'Register Content';
                        }
                    }
                }
            })

            .state('unauthenticated.dashboard.help',{
                url: '/help',
                views: {
                    'contentView@': {
                        templateUrl: '/static/fangulitic/partials/dashboard/unauthenticated/layout/content.html',
                        controller: function($scope, $stateParams, DashService){
                            $scope.dashTitle = 'help';
                            $scope.dashContent = 'Help Content';
                        }
                    }
                }
            });

    }
);

Fangulitic.constant('authUrl',
    'http://localhost:5000/auth/login'
);