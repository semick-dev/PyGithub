import Framework

import datetime

class IssueComment( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.comment = self.g.get_user().get_repo( "PyGithub" ).get_issue( 28 ).get_comment( 5808311 )

    def testAttributes( self ):
        self.assertEqual( self.comment.body, "Comment created by PyGithub" )
        self.assertEqual( self.comment.created_at, datetime.datetime( 2012, 5, 20, 11, 46, 42 ) )
        self.assertEqual( self.comment.id, 5808311 )
        self.assertEqual( self.comment.updated_at, datetime.datetime( 2012, 5, 20, 11, 46, 42 ) )
        self.assertEqual( self.comment.url, "https://api.github.com/repos/jacquev6/PyGithub/issues/comments/5808311" )
        self.assertEqual( self.comment.user.login, "jacquev6" )

    def testEdit( self ):
        self.comment.edit( "Comment edited by PyGithub" )
        self.assertEqual( self.comment.body, "Comment edited by PyGithub" )
        self.assertEqual( self.comment.updated_at, datetime.datetime( 2012, 5, 20, 11, 53, 59 ) )

    def testDelete( self ):
        self.comment.delete()
