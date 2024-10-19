// CommandBuilder.cpp
#include "CommandBuilder.h"

#include <sstream>

#include "Utils.h"

namespace MediaProcessor {

void CommandBuilder::addArgument(const std::string& arg) {
    m_arguments.push_back(arg);
}

void CommandBuilder::addFlag(const std::string& flag) {
    m_arguments.push_back(flag);
}

void CommandBuilder::addFlag(const std::string& flag, const std::string& value) {
    m_arguments.push_back(flag);
    m_arguments.push_back(value);
}

std::string CommandBuilder::build() const {
    std::ostringstream command;
    for (const auto& arg : m_arguments) {
        command << formatArgument(arg) << ' ';
    }
    std::string commandStr = command.str();

    return Utils::trimTrailingSpace(commandStr);
}

std::string CommandBuilder::formatArgument(const std::string& arg) const {
    using MediaProcessor::Utils::containsWhitespace;

    if (containsWhitespace(arg)) {
        return "\"" + arg + "\"";
    }
    return arg;
}

}  // namespace MediaProcessor