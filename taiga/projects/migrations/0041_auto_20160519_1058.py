# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-19 10:58
from __future__ import unicode_literals

from django.db import migrations
import djorm_pgarray.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0040_remove_memberships_of_cancelled_users_acounts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='public_permissions',
            field=djorm_pgarray.fields.TextArrayField(choices=[('view_project', 'View project'), ('view_milestones', 'View milestones'), ('add_milestone', 'Add milestone'), ('modify_milestone', 'Modify milestone'), ('delete_milestone', 'Delete milestone'), ('view_us', 'View user story'), ('add_us', 'Add user story'), ('modify_us', 'Modify user story'), ('comment_us', 'Comment user story'), ('delete_us', 'Delete user story'), ('view_tasks', 'View tasks'), ('add_task', 'Add task'), ('modify_task', 'Modify task'), ('comment_task', 'Comment task'), ('delete_task', 'Delete task'), ('view_issues', 'View issues'), ('add_issue', 'Add issue'), ('modify_issue', 'Modify issue'), ('comment_issue', 'Comment issue'), ('delete_issue', 'Delete issue'), ('view_wiki_pages', 'View wiki pages'), ('add_wiki_page', 'Add wiki page'), ('modify_wiki_page', 'Modify wiki page'), ('comment_wiki_page', 'Comment wiki page'), ('delete_wiki_page', 'Delete wiki page'), ('view_wiki_links', 'View wiki links'), ('add_wiki_link', 'Add wiki link'), ('modify_wiki_link', 'Modify wiki link'), ('delete_wiki_link', 'Delete wiki link')], dbtype='text', default=[], verbose_name='user permissions'),
        ),
    ]