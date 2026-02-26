# Epic Title: Establish Scalable Infrastructure using Next.js, Node.js, and PostgreSQL

module.exports = {
    reactStrictMode: true,
    async rewrites() {
        return [
            {
                source: '/api/:path*',
                destination: 'http://localhost:4000/api/:path*',
            },
        ];
    },
};