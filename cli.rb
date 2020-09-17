require "bundler/setup"
require "dry/cli"
require "find"

module Acio
  module CLI
    module Commands
      extend Dry::CLI::Registry

      class Version < Dry::CLI::Command
        desc "Print version"

        def call(*)
          puts "0.0.1-beta"
        end
      end

      class Build < Dry::CLI::Command
        desc "Builds a Jekyll Site in the current directory"

        def call(*)

        end
      end


      register "version", Version, aliases: ["v", "-v", "--version"]
      register "build",    Build

    end
  end
end

Dry::CLI.new(Foo::CLI::Commands).call