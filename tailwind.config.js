/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./templates/**/*.html',
        './static/src/**/*.js',
        './blog/**/*.html',
        './blog/**/*.py',
        './node_modules/flowbite/**/*.js'],
    darkMode: 'class',
    theme: {
        extend: {},
    },
    plugins: [
        require("daisyui"),
        require('flowbite-typography'),
        require('flowbite/plugin')({
            wysiwyg: true,
        }),
        require('flowbite/plugin'),
        function ({addUtilities}) {
            addUtilities({
                '.bg-custom-pattern': {
                    'background-color': '#FAE7F4',
                    'opacity': '1.3',
                    'background': `
            radial-gradient(circle, transparent 20%, #f0b8f7 20%, #f0b8f7 80%, transparent 80%, transparent),
            radial-gradient(circle, transparent 20%, #f0b8f7 20%, #f0b8f7 80%, transparent 80%, transparent) 25px 25px,
            linear-gradient(#ffffff 2px, transparent 2px) 0 -1px,
            linear-gradient(90deg, #ffffff 2px, #f0b8f7 2px) -1px 0
          `,
                    'background-size': '50px 50px, 50px 50px, 25px 25px, 25px 25px',
                },
            });
        },
    ],
    daisyui: {
        themes: ["valentine"],
        darkTheme: "dark", // name of one of the included themes for dark mode
        base: true, // applies background color and foreground color for root element by default
        styled: true, // include daisyUI colors and design decisions for all components
        utils: true, // adds responsive and modifier utility classes
        prefix: "", // prefix for daisyUI classnames (components, modifiers and responsive class names. Not colors)
        logs: true, // Shows info about daisyUI version and used config in the console when building your CSS
        themeRoot: ":root", // The element that receives theme color CSS variables
    },
}

