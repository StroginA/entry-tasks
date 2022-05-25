const queryCourses = (courses, priceRange) => {
	/* 
	If priceRange has an overlap with a course's price range (inclusive), includes it.
	Sorts output by lower end of the bracket (null first) then higher (null last), ascending.
	*/
	const output = [];
	for (course of courses) {
		if (
		(!priceRange[0] || !course.prices[1] || priceRange[0] <= course.prices[1])
		&&
		(!priceRange[1] || !course.prices[0] || priceRange[1] >= course.prices[0])
		) {
			output.push(course);
		};
	};
	output.sort((a, b) => {
		if (a.prices[0] !== b.prices[0]) {
			return (
			(a.prices[0] === null) ? 
			-1 : 
			(b.prices[0] === null) ? 
			1 : 
			a.prices[0] - b.prices[0]
			);
		} else {
			return (
			(a.prices[1] === null) ? 
			1 : 
			(b.prices[1] === null) ? 
			-1 : 
			a.prices[1] - b.prices[1]
			);
		}
	});
	return output;	
};



let courses = [
	{ name: "Courses in England", prices: [0, 100] }, 
	{ name: "Courses in Germany", prices: [500, null] }, 
	{ name: "Courses in Italy", prices: [100, 200] }, 
	{ name: "Courses in Russia", prices: [null, 400] },
	{ name: "Courses in China", prices: [50, 250] },
	{ name: "Courses in USA", prices: [200, null] },
	{ name: "Courses in Kazakhstan", prices: [56, 324] },
	{ name: "Courses in France", prices: [null, null] },
];

let requiredRange1 = [null, 200];
let requiredRange2 = [100, 350];
let requiredRange3 = [200, null];


console.log(queryCourses(courses, requiredRange1));
console.log(queryCourses(courses, requiredRange2));
console.log(queryCourses(courses, requiredRange3));