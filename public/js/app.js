(function(){

	// Global map
	var map = null;

	// Define Model for Backbone
	var EndpointModel = Backbone.Model.extend({
		idAttribute: 'id'
	});

	// Define collection for backbone
	var EndpointCollection = Backbone.Collection.extend({
		model: EndpointModel,
		url: '/endpoints'
	});

	// The list of endpoints
	var endpoint_objs = new EndpointCollection();
	var marker_element_objs = {};

	var create_marker = function(endpoint_obj) {

		var marker = new google.maps.Marker({
	      position: new google.maps.LatLng(endpoint_obj.get('lat'),endpoint_obj.get('lng')),
	      title: endpoint_obj.get('title'),
	      icon: '/img/' + endpoint_obj.get('icon') + '-marker.png',
	      animation: google.maps.Animation.DROP
	  });

		return marker;

	};

	// Handle the events
	endpoint_objs.on('add', function(endpoint_obj){

		var endpoint_id = endpoint_obj.get('id');

		if(!marker_element_objs[ endpoint_id ]) {

			var marker_el = create_marker(endpoint_obj);
			marker_element_objs[ endpoint_id ] = marker_el;

			setTimeout(function(){

				marker_el.setMap(map);

			}, 200);

		}

	});

	// Handle the events
	endpoint_objs.on('change', function(endpoint_obj){

		var endpoint_id = endpoint_obj.get('id');
		if(marker_element_objs[ endpoint_id ])
			marker_element_objs[ endpoint_id ].setMap(null);

		var marker_el = create_marker(endpoint_obj);
		marker_element_objs[ endpoint_id ] = marker_el;

		setTimeout(function(){

			marker_el.setMap(map);

		}, 200);


	});

	// Handle the events
	endpoint_objs.on('remove', function(endpoint_obj){

		var endpoint_id = endpoint_obj.get('id');

		if(marker_element_objs[ endpoint_id ]) {

			marker_element_objs[ endpoint_id ].setMap(null);
			delete marker_element_objs[ endpoint_id ];

		}

	});

	// Handles syncing
	var handle_sync = function() {

		// fetch it
		endpoint_objs.fetch();

		// Again in 10 seconds
		setTimeout(handle_sync, 1000);

	};

	// Do it !
	handle_sync();

	function init() {
		// Basic options for a simple Google Map
		// For more options see: https://developers.google.com/maps/documentation/javascript/reference#MapOptions
		var mapOptions = {
		    // How zoomed in you want the map to start at (always required)
		    zoom: 11,

		    // The latitude and longitude to center the map (always required)
		    center: new google.maps.LatLng(-33.922381,18.418044), // Cape Town

		    // How you would like to style the map. 
		    // This is where you would paste any style found on Snazzy Maps.
		    styles: [{'featureType':'water','stylers':[{'visibility':'on'},{'color':'#acbcc9'}]},{'featureType':'landscape','stylers':[{'color':'#f2e5d4'}]},{'featureType':'road.highway','elementType':'geometry','stylers':[{'color':'#c5c6c6'}]},{'featureType':'road.arterial','elementType':'geometry','stylers':[{'color':'#e4d7c6'}]},{'featureType':'road.local','elementType':'geometry','stylers':[{'color':'#fbfaf7'}]},{'featureType':'poi.park','elementType':'geometry','stylers':[{'color':'#c5dac6'}]},{'featureType':'administrative','stylers':[{'visibility':'on'},{'lightness':33}]},{'featureType':'road'},{'featureType':'poi.park','elementType':'labels','stylers':[{'visibility':'on'},{'lightness':20}]},{},{'featureType':'road','stylers':[{'lightness':20}]}]
		};

		// Get the HTML DOM element that will contain your map 
		// We are using a div with id="map" seen below in the <body>
		var mapElement = document.getElementById('map-canvas');

		// Create the Google Map using out element and options defined above
		map = new google.maps.Map(mapElement, mapOptions);
	}

	// When the window has finished loading create our google map below
	google.maps.event.addDomListener(window, 'load', init);

})();