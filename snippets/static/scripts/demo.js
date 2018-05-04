var myApp = angular.module("myApp", []);
myApp.config(function($interpolateProvider) {
$interpolateProvider.startSymbol('[[');
$interpolateProvider.endSymbol(']]');
});

myApp.controller("MyController", ["$scope","$location","$http", function($scope, $location, $http) {
$scope.myName = "Hakim Adil Will Win in Django";
$scope.GetData=function(){
console.log($location.$$host)
 //$http.get('http://'+$location.$$host+':'+$location.$$port+'/Catalog/validate_username/',

 $http.get('http://localhost:8000/snippets/post',
                       {
                       }).success(function (data) {
                          $scope.DatedVault= data;
console.log($scope.DatedVault)
console.log('http://'+$location.$$host+':'+$location.$$port+'/snippets/post')
                       }).error(function (error, status) {
console.log('http://'+$location.$$host+':'+$location.$$port+'/snippets/post')
                       });
                       };

                       $scope.PostBook=function(){
                                   var BookObj=[
                                   {'title':'Angular-java',
                                   'summary':'connection django and angular',
                                   'isbn':'1154758',
                                   'author_id':"1"},
                                    {'title':'Angular-PHP',
                                   'summary':'connection Asp.Net and angular',
                                   'isbn':'11547845',
                                   'author_id':"1"},
                                    {'title':'Angular-Ruby',
                                   'summary':'connection Node and angular',
                                   'isbn':'11545478',
                                   'author_id':"1"},
                                  ]
                            $http({
                            method: 'POST',
                            url: $location.$$protocol+'://'+$location.$$host+'/Catalog/'+'validate_username/',
                            data: $.param({ deal: JSON.stringify(BookObj) }),
                            headers: { 'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8' }
                        }).success(function (data, status, headers, config) {
                        $scope.DatedVault= data;

                        }).error(function (data, status, headers, config) {
                            // handle error things
                        });

                       };
                       $scope.GetData();
}]);