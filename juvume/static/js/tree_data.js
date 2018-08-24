var root = {'children': [{'amenities': ['Lockers/Robes', 'Steam/Sauna', 'Showers', 'Pool'], 'children': [{'supported': false, 'name': 'Therapeutic'}, {'supported': false, 'name': 'Thai'}, {'supported': false, 'name': 'Hot Stone'}, {'supported': false, 'name': 'Reflexology'}], 'name': 'Massage'}, {'amenities': ['Lockers/Robes'], 'name': 'Face', 'children': [{'supported': false, 'name': 'Facials'}, {'name': 'Lashes & Brows', 'children': [{'supported': false, 'name': 'Lash Extensions'}, {'supported': false, 'name': 'Lash Tinting'}, {'supported': false, 'name': 'Brow Tinting'}]}, {'name': 'Peels', 'children': [{'supported': false, 'name': 'Microdermabrasion'}, {'supported': false, 'name': 'Chemical Peels'}]}, {'name': 'Medi', 'children': [{'supported': false, 'name': 'Facial Fillers'}, {'supported': false, 'name': 'Laser Facials'}, {'supported': false, 'name': 'BOTOX'}]}, {'name': 'Make Up', 'children': [{'supported': false, 'name': 'Application'}, {'supported': false, 'name': 'Permanent Makeup'}]}]}, {'amenities': ['Wine'], 'children': [{'supported': false, 'name': 'Womens Cut'}, {'supported': false, 'name': 'Conditioning Treatments'}, {'supported': false, 'name': 'Blowout'}, {'supported': false, 'name': 'Updo'}, {'supported': false, 'name': 'Extensions'}, {'supported': false, 'name': 'Straightening'}, {'supported': false, 'name': 'Mens Cut'}], 'name': 'Hair'}, {'amenities': ['Wine'], 'children': [{'name': 'Waxing', 'children': [{'supported': false, 'name': 'Brows/Face'}, {'supported': false, 'name': 'Bikini/Brazilian'}, {'supported': false, 'name': 'Body'}, {'supported': false, 'name': 'Mens'}]}, {'supported': false, 'name': 'Laser'}, {'supported': false, 'name': 'Threading'}, {'supported': false, 'name': 'Sugaring'}, {'supported': false, 'name': 'Electrolysis'}], 'name': 'Hair Removal'}, {'amenities': ['Wine'], 'children': [{'supported': false, 'name': 'Pedicure'}, {'supported': false, 'name': 'Manicure'}, {'supported': false, 'name': 'Mani/pedi'}, {'supported': false, 'name': 'Polish Change'}, {'supported': false, 'name': 'Gels'}, {'supported': false, 'name': 'Acrylics'}], 'name': 'Nails'}, {'amenities': ['Lockers/Robes', 'Steam/Sauna', 'Showers', 'Pool'], 'children': [{'supported': false, 'name': 'Yoga'}, {'supported': false, 'name': 'Pilates'}, {'supported': false, 'name': 'Cross Training Classes'}, {'supported': false, 'name': 'Cycling Classes'}, {'supported': false, 'name': 'TRX'}, {'supported': false, 'name': 'Flexibility/Stretching Classes'}, {'supported': false, 'name': 'Outdoor Bootcamp'}, {'supported': false, 'name': 'Abs & Targeted Area Classes'}, {'supported': false, 'name': 'Personal Training'}], 'name': 'Fitness'}, {'amenities': [], 'children': [{'supported': false, 'name': 'Chiropractic'}, {'supported': false, 'name': 'Actupuncture'}, {'supported': false, 'name': 'Colonics'}, {'supported': false, 'name': 'Weight Loss'}], 'name': 'Alternative Wellness'}, {'amenities': ['Showers'], 'children': [{'supported': false, 'name': 'Tanning', 'children': [{'supported': false, 'name': 'Spray Tan'}, {'supported': false, 'name': 'Tanning Beds'}]}, {'supported': false, 'name': 'Scrubs'}, {'supported': false, 'name': 'Wraps'}, {'supported': false, 'name': 'Back Facials'}], 'name': 'Body Treatments'}, {'amenities': [], 'children': [{'supported': false, 'name': 'Cleaning'}, {'supported': false, 'name': 'Whitening'}], 'name': 'Dental'}], 'name': 'user'};
root.children = _.map(root.children, function(n) { return new SpaProcedure(n); });
// Prep root for "reverse" lookup.
attach_parents(root);
