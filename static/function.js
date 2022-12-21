    // Get the modal
    var modal = document.getElementById("myModal");
    // Get the button that opens the modal
    var btn = document.getElementById("myBtn");
    
    // checking if page has been already visited showing modal 5 seconds after page loads 
    const popup = document.querySelector("#myModal");


  //whatever you want it to do if they have visited
  window.addEventListener("load", function(){
	showform();
 });
 
 function showform(){
   const timelimit = 5 ;
   let i = 0; 
   const timer = setInterval(function(){
	 i++;
	 if (i == timelimit){
	   clearInterval(timer);
	   popup.style.display = "block";
	 }
   }, 5000);
 }


 
//     let hasVisited = localStorage.getItem('visited')
//     if( !hasVisited){
//   //whatever you want it to do if they have visited
//   window.addEventListener("load", function(){
//        showform();
//     });
    
//     function showform(){
//       const timelimit = 5 ;
//       let i = 0; 
//       const timer = setInterval(function(){
//         i++;
//         if (i == timelimit){
//           clearInterval(timer);
//           popup.style.display = "block";
//         }
//       }, 1000);
//     }
//   localStorage.setItem('visited', true);
// }