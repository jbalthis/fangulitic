'use strict';
/**
 * controllers
 */



Fangulitic.controller('DropdownCtrl', function($scope, NavService){
    $scope.platforms = NavService.getPlatforms();
});

Fangulitic.controller('SidebarCtrl', function($scope, DashService){
    $scope.sidebarLinks = DashService.getSideBarLinks();
});

Fangulitic.controller('AuthCtrl', function($scope, $http, $location, authUrl){

    $scope.authenticate = function(user, pass){
        $http.post(authUrl,
            {
                username: user,
                password: pass
            },
            {
                withCredentials: true
            })
            .success(function(data){
                $location.path('/main');
            })
            .error(function(error){
                $scope.authenticationError = error;
            });
    }

});