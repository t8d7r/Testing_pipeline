import git
from unidiff import PatchSet

from io import StringIO
import sys

#commit_sha1 = 'commit_sha'
commit_sha1 = sys.argv[0]

repo_directory_address = "./"

repository = git.Repo(repo_directory_address)
commit = repository.commit(commit_sha1)

uni_diff_text = repository.git.diff(commit_sha1+ '~1', commit_sha1,
                                    ignore_blank_lines=True, 
                                    ignore_space_at_eol=True)

patch_set = PatchSet(StringIO(uni_diff_text), encoding='utf-8')

change_list = []  # list of changes 
                  # [(file_name, [row_number_of_deleted_line],
                  # [row_number_of_added_lines]), ... ]

for patched_file in patch_set:
    file_path = patched_file.path  # file name
    print('file name :' + file_path)
    del_line_no = [line.target_line_no 
                   for hunk in patched_file for line in hunk 
                   if line.is_added and
                   line.value.strip() != '']  # the row number of deleted lines
    print('deleted lines : ' + str(del_line_no))
    ad_line_no = [line.source_line_no for hunk in patched_file 
                  for line in hunk if line.is_removed and
                  line.value.strip() != '']   # the row number of added liens
    print('added lines : ' + str(ad_line_no))
    change_list.append((file_path, del_line_no, ad_line_no))

