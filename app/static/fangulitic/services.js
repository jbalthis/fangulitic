'use strict';

Fangulitic.service('NavService', function(){

    this.getPlatforms = function(){
        return [
            'routing',
            'switching',
            'wireless'
        ]
    };

});


Fangulitic.service('DashService', function(){

    this.getDashboard = function(dashTitle){

            this.dashboard = 'Dashboard Content';

            this.pages = 'Pages Content';

            this.forum = 'Forum Content';

            this.contacts = 'Contacts Content';

            this.metrics = 'Metrics Content';

            this.admin = 'Admin Content';

            this.help = 'Help Content';


            switch(dashTitle){

                case "dashboard":
                    return this.dashboard;

                case "pages":
                    return this.pages;

                case "forum":
                    return this.forum;

                case "contacts":
                    return this.contacts;

                case "metrics":
                    return this.metrics;

                case "admin":
                    return this.admin;

                case "help":
                    return this.help;

                default:
                    return this.dashboard;

            }
    };


    this.getSideBarLinks = function(){
        return [
            'dashboard',
            'pages',
            'forum',
            'contacts',
            'metrics',
            'admin',
            'help'
        ];
    };


    this.getPageList = function(){
      return [
          'platforms',
          'solutions',
          'services',
          'training',
          'competitive'
      ]
    };

});