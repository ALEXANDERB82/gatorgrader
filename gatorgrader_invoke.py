""" Invokes programs on the command-line on behalf of GatorGrader """

import gatorgrader
import gatorgrader_comments
import gatorgrader_fragments
import gatorgrader_entities
import gatorgrader_files
import gatorgrader_util

SINGLE = "single-line"
MULTIPLE = "multiple-line"


def invoke_all_file_in_directory_checks(files, directories):
    """ Repeatedly perform the check and return the results """
    print("Checking if files are in the expected directories ...")
    print()
    was_file_found_list = []
    for filecheck, directory in zip(files, directories):
        was_file_found = invoke_file_in_directory_check(filecheck, directory)
        was_file_found_list.append(was_file_found)
    print()
    print("... Done checking if files are in the expected directories")
    return was_file_found_list


def invoke_file_in_directory_check(filecheck, directory):
    """ Check to see if the file is in the directory """
    gatorgrader_home, had_to_set_gatorgrader_home = gatorgrader.get_gatorgrader_home(
    )
    was_file_found = gatorgrader_files.check_file_in_directory(
        filecheck, gatorgrader_home + directory)
    print(
        "Was ",
        filecheck,
        " found in ",
        directory,
        "? ",
        gatorgrader_util.get_human_answer(was_file_found),
        sep="")
    return was_file_found


def invoke_all_comment_checks(files, directories, expected_counts,
                              comment_type):
    """ Repeatedly perform the check and return the results """
    print("Checking for", comment_type, "comments...")
    print()
    was_exceeded_list = []
    met_or_exceeded_count = 0
    for filecheck, directory, expected_count in zip(files, directories,
                                                    expected_counts):
        if comment_type == SINGLE:
            met_or_exceeded_count = gatorgrader_entities.entity_greater_than_count(
                filecheck, directory, expected_count,
                gatorgrader_comments.count_singleline_java_comment)
        elif comment_type == MULTIPLE:
            met_or_exceeded_count = gatorgrader_entities.entity_greater_than_count(
                filecheck, directory, expected_count,
                gatorgrader_comments.count_multiline_java_comment)

        was_exceeded_list.append(met_or_exceeded_count)
        print(
            "Did ",
            filecheck,
            " in ",
            directory,
            " have ",
            expected_count,
            " ",
            comment_type,
            " comments? ",
            gatorgrader_util.get_human_answer(met_or_exceeded_count),
            sep="")

    print()
    print("... Done checking for", comment_type, "comments")
    return was_exceeded_list


def invoke_all_paragraph_checks(files, directories, expected_counts):
    """ Repeatedly perform the check and return the results """
    print("Checking for paragraphs...")
    print()
    was_exceeded_list = []
    met_or_exceeded_count = 0
    for filecheck, directory, expected_count in zip(files, directories,
                                                    expected_counts):
        met_or_exceeded_count = gatorgrader_entities.entity_greater_than_count(
            filecheck, directory, expected_count,
            gatorgrader_fragments.count_paragraphs)

        was_exceeded_list.append(met_or_exceeded_count)
        print(
            "Did ",
            filecheck,
            " in ",
            directory,
            " have ",
            expected_count,
            " paragraphs? ",
            gatorgrader_util.get_human_answer(met_or_exceeded_count),
            sep="")

    print()
    print("... Done checking for paragraphs")
    return was_exceeded_list


def invoke_all_fragment_checks(files, directories, fragments, expected_counts):
    """ Repeatedly perform the check and return the results """
    print("Checking for fragments...")
    print()
    was_exceeded_list = []
    met_or_exceeded_count = 0
    for filecheck, directory, fragment, expected_count in zip(files, directories, fragments,
                                                              expected_counts):
        met_or_exceeded_count = gatorgrader_entities.specified_fragment_greater_than_count(
            filecheck, directory, fragment, expected_count,
            gatorgrader_fragments.count_specified_fragment)

        was_exceeded_list.append(met_or_exceeded_count)
        print(
            "Did ",
            filecheck,
            " in ",
            directory,
            " have ",
            expected_count,
            " of the fragment \"",
            fragment,
            "\" fragment? ",
            gatorgrader_util.get_human_answer(met_or_exceeded_count),
            sep="")

    print()
    print("... Done checking for fragments")
    return was_exceeded_list

