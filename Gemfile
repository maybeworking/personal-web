source "https://rubygems.org"

# Uncomment the line below if you want to use Jekyll version 3.9
gem "jekyll", "~> 3.9.0", group: :jekyll_plugins

# Jekyll plugins can be added here
group :jekyll_plugins do
   gem "jekyll-paginate", "~> 1.1.0"
   gem "jekyll-redirect-from", "~> 0.16.0"
 end

# Use GitHub Pages plugin
gem "github-pages", "~> 231"

# added for netlify
gem "gem_name", "version"
gem "bigdecimal"
gem "csv"

# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
install_if -> { RUBY_PLATFORM =~ %r!mingw|mswin|java! } do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.0", :install_if => Gem.win_platform?

# HTTP server for local tests
gem "webrick", "~> 1.7"
