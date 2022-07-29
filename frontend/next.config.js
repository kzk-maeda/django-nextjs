/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  env: {
    // API_URL: "http://api:8000",
    API_URL: "https://jobbee-kzk.herokuapp.com",
  },
};

module.exports = nextConfig;
