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