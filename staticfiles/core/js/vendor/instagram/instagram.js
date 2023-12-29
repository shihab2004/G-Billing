var feed = new Instafeed({
			target: 'instafeed',
			get: 'user',
			userId: '5651689605',
			tagName: 'awesome',		
			limit:'16',
			links:'false',		
			clientId: '3171206d1cd04434aae1aa51e5f63137',
			accessToken: '5651689605.1677ed0.28e806f023b44cf796115947959cae7e',
			});
			feed.run();